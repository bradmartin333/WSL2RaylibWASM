# MountainClimber
Mountain climbing game made with RayLib and emscripten for WASM

## WSL2 Setup
- Exit all windows and open Command Prompt as admin
    - `wsl --update` to enable X11 server
- Python3 comes with WSL2, so we don't have to install that
- Install CMake and build tools
    - `sudo apt-get update && sudo apt-get install cmake build-essential`
- Install emscripten from source
    - `cd ~`
    - `git clone https://github.com/emscripten-core/emsdk.git`
    - `cd emsdk/`
    - `./emsdk install latest`
    - `./emsdk activate latest`
- Install raylib from source
    - Install deps
        - `sudo apt install vlc libasound2-dev libx11-dev libxrandr-dev libxi-dev libgl1-mesa-dev libglu1-mesa-dev libxcursor-dev libxinerama-dev`
    - `cd ~`
    - `git clone https://github.com/raysan5/raylib.git raylib`
    - `cd raylib`
    - `mkdir build && cd build`
    - `cmake -DBUILD_SHARED_LIBS=ON ..`
    - `make`
    - `sudo make install`
    - `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib`
    - `export DISPLAY=:0`
    - Edit `/home/$USER/raylib/src/Makefile`
        - Update `EMSDK_PATH` to be `/home/$(USER)/emsdk`
- Build `main.cpp` executable named `test`
    -  `g++ main.cpp -lraylib -o test`
- Build `main.cpp` for wasm
    - `cd ~/MountainClimber`
    - `source ../emsdk/emsdk_env.sh && emcc main.cpp -o ./build/game.html -Wall -std=c++14 -D_DEFAULT_SOURCE -Wmissing-braces -Wunused-result -Os -I. -I ../raylib/src/ -I ../raylib/src/external/ -L. -L ../raylib/src/ -s USE_GLFW=3 -s ASYNCIFY -s TOTAL_MEMORY=67108864 -s FORCE_FILESYSTEM=1 --shell-file ./build/shell.html ../raylib/src/libraylib.a  -DPLATFORM_WEB -s EXPORTED_FUNCTIONS=[\"_free\",\"_malloc\",\"_main\"] -s EXPORTED_RUNTIME_METHODS=ccall --preload-file res/@res/`
        - The first command could be automated elsewhere, but this keeps it repeatable in a WSL environment
    - Open `build/game.html` in a live server
