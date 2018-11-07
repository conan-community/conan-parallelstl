#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools


class PSTLConan(ConanFile):
    name = "parallelstl"
    version = "20181004"
    author = "Conan Community"
    description = "C++ standard library algorithms with support for execution policies"
    homepage = "https://github.com/intel/parallelstl"
    url = "https://github.com/conan-community/conan-parallelstl"
    topics = ("conan", "parallelstl", "stl", "algorithms", "parallel")
    license = "Apache-2.0"
    exports = "LICENSE"
    no_copy_sources = True
    options = {"backend": ["tbb", False]}
    default_options = {"backend": "tbb"}
    _source_subfolder = "source_subfolder"

    def source(self):
        tools.get("%s/archive/%s.tar.gz" % (self.homepage, self.version))
        os.rename("%s-%s" % (self.name, self.version), self._source_subfolder)

    def requirements(self):
        if self.options.backend == "tbb":
            self.requires("TBB/2019_U1@conan/stable")

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=os.path.join(self._source_subfolder, "include"))
  
    def package_id(self):
        self.info.header_only()

    def package_info(self):
        if self.options.backend == "tbb":
            self.cpp_info.defines.append("__PSTL_USE_TBB")
