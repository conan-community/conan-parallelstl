#!/usr/bin/env python
# -*- coding: utf-8 -*-

import platform
from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    if platform.system() == "Windows":
        builder.add(settings={"compiler":"Visual Studio", "compiler.version": "15",
                              "arch": "x86", "build_type": "Release"},
                    options={}, env_vars={}, build_requires={})
    elif platform.system() == "Linux":
        builder.add(settings={"compiler":"gcc", "compiler.version": "7",
                              "arch": "x86_64", "build_type": "Release"},
                    options={}, env_vars={}, build_requires={})
    builder.run()
