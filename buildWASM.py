import os
import argparse

cwd = os.getcwd()

argParser = argparse.ArgumentParser(
    prog='Raylib WASM builder',
    description='Uses emcc',
    epilog='Requires setup of Raylib (youtu.be/-F6THkPkF2I) and emcc (youtu.be/j6akryezlzc)')
args = vars(argParser.parse_args())

inputPath = "MountainClimber\MountainClimber.cpp"
if not os.path.exists(inputPath):
    print('Input path {} does not exist'.format(inputPath))
    exit(0)
outputPath = os.path.join(cwd, 'game.html')

# Build WASM
raylibSrcDir = 'C:/raylib/raylib/src'
compilerArgs = "-Wall -std=c++14 -D_DEFAULT_SOURCE -Wno-missing-braces -Wunused-result -Os -I. -I {0} -I {0}/external -L. -L {0} -s USE_GLFW=3 -s ASYNCIFY -s TOTAL_MEMORY=67108864 -s FORCE_FILESYSTEM=1 --shell-file ./shell.html {0}/web/libraylib.a -DPLATFORM_WEB -s EXPORTED_FUNCTIONS=[\"_free\",\"_malloc\",\"_main\"] -s EXPORTED_RUNTIME_METHODS=ccall".format(
    raylibSrcDir)
build_cmd = "emcc -o {} {} {}".format(outputPath, inputPath, compilerArgs)
os.system(build_cmd)
