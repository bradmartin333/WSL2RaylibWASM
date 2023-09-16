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
    - `./wasm_build.sh`
    - Open `build/game.html` in a live server
