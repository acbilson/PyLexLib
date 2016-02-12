import os
import sys

class FileWalker(object):

  """ walks through a directory, with the capacity to find and replace strings within files """

  DEBUG = False
  BACKUP = False

  def __init__(self):
    self.walkDirectory = ""
    self.files = []
    self.history = {}

  def walk(self, startingDirectory, condition=None):

    """ recurses through all directories, returning the absolute path of every file that meets the specified condition """

    self.walkDirectory = self._convert_to_absolute_path(startingDirectory)
    self.files = self._get_all_files(self.walkDirectory, condition)

    return self.walkDirectory, self.files

  def backup_all(self, startingDirectory, file_func=None):

    """ backs up an entire directory, which is useful if there will be multiple changes to a single file 

        Note: use a new instance of FileWalker to store backup to avoid overwrite """

    if file_func == None:
      file_func = self._set_func_if_none(file_func)

    self.walkDirectory = self._convert_to_absolute_path(startingDirectory)

    for root, subdirs, files in os.walk(self.walkDirectory):
      filePaths = self._get_full_paths(root, files)
      for path in filePaths:
        if file_func(path):
          with open(path, 'r') as f:
            content = f.read()
            self.backup(path, content)

  def backup(self, file, content):

    """ backs up walked file in case something goes wrong """

    self._add_to_history(file, content)

    if self.DEBUG == True:
      self.__debug_backup(file, content)

  def replace(self, condition):
    
    """ replaces every instance of a particular string in each walked file's contents with the specified string """

    totalReplacements = 0

    if self.DEBUG == True:
      self.__debug_replace_intro(walkDir, condition)
 
    for file in self.files:

      # Read file
      with open(file, 'r') as f:
        content = f.read()

      if self.BACKUP == True:
        self.backup(file, content)

      for replacement in condition.replacements:
        # Check contents for text
        if replacement.textToFind in content:
          totalReplacements = totalReplacements + 1
          content = content.replace(replacement.textToFind, replacement.textToReplace)

      if self.DEBUG == True:
        self.__debug_replace(content, totalReplacements)

      # Write file
      with open(file, 'w') as f:
        f.write(content)
  
    return totalReplacements

  def revert(self):

    """ If the last change isn't what you wanted, will restore all files to their previous revision """

    for file, content in self.history.items():
      with open(file, 'w') as f:
        f.write(content)

      if self.DEBUG == True:
        self.__debug_revert(file, content)

  def _add_to_history(self, fileName, fileContent):
    self.history[fileName] = fileContent

  def _get_all_files(self, directory, condition=None):

    """ returns all files recursively beginning at the start directory 'walk_dir' """

    allFiles = []
    for root, subdirs, files in os.walk(directory):
      if condition.dirFunc(root):
        csFiles = self._get_files_from_func(files, condition.func)
        absFiles = self._get_full_paths(root, csFiles)
        allFiles.extend(absFiles)
    return allFiles

  def _convert_to_absolute_path(self, path):
    return os.path.abspath(path)

  def _get_files_from_func(self, files, file_func=None):
    
    if condition == None:
      # condition will return everything
      file_func = self._set_func_if_none(file_func)
      file_func = lambda f: 1 == 1
    return [f for f in files if file_func(f)]

  def _get_full_paths(self, root, files):

    """ returns a list of files with full absolute paths """

    abs_root = self._convert_to_absolute_path(root)
    return [os.path.join(abs_root, f) for f in files]

  def _set_func_if_none(self, func):
    # Always true
    func = lambda f: 1 == 1
    return func

  # for DEBUG == True only
  def __debug_replace_intro(self, walkDir, condition):
    print("\n-----------------DEBUG-----------------")
    print("\tRecursing at: " + walkDir)
    print("\n\tYou will replace:")
    for replacement in condition.replacements:
      print("\n\tthis: " + replacement.textToFind)
      print("\twith:    " + replacement.textToReplace)
    print("\n\tin: " + condition.description)

  def __debug_backup(self, file, content):
    print("\tBacked up: ")
    print("\tPath: " + file)
    print("\tContent Length: " + str(len(content)))

  def __debug_replace(self, content, totalReplacements):
    print("\tNew Content Length: " + str(len(content)) + "; Current Replacements: " + str(totalReplacements))

  def __debug_revert(self, file, content):
    print("\tReverted: ")
    print("\tPath: " + file)
    print("\tContent Length: " + str(len(content)))
    print("-----------------DEBUG-----------------\n")

class Replacement(object):

  def __init__(self, textToFind, textToReplace):
    self.textToFind = textToFind
    self.textToReplace = textToReplace

class Condition(object):

  def __init__(self, name, description, conditionFunc, replacements, directoryFunc=None, expectedReplacements=0):
    self.name = name
    self.description = description
    self.func = conditionFunc
    self.replacements = replacements
    if directoryFunc == None:
      directoryFunc = lambda f: 1 == 1
    self.dirFunc = directoryFunc
    self.expectedReplacements = expectedReplacements
