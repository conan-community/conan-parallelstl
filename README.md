# Conan ParallelSTL

[![Download](https://api.bintray.com/packages/conan-community/conan/ParallelSTL%3Aconan/images/download.svg)](https://bintray.com/conan-community/conan/ParallelSTL%3Aconan/_latestVersion)
[![Build Status](https://travis-ci.org/conan-community/conan-ParallelSTL.svg?branch=release%2F20181004)](https://travis-ci.org/conan-community/conan-ParallelSTL)
[![Build status](https://ci.appveyor.com/api/projects/status/github/conan-community/conan-ParallelSTL?svg=true)](https://ci.appveyor.com/project/conan-community/conan-ParallelSTL)

[Conan.io](https://conan.io) package recipe for [ParallelSTL](https://github.com/intel/parallelstl) project.

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/conan-community/conan/ParallelSTL%3Aconan).

## For Users: Use this package

### Basic setup

    $ conan install ParallelSTL/20181004@conan/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    ParallelSTL/20181004@conan/stable

    [generators]
    cmake

## License

[MIT License](LICENSE)
