# WSL2 Raylib WASM
Example C++ game made with RayLib and emscripten on WSL2

## WSL2 Setup
- Click the windows icon in the toolbar and type `Turn Windows features on or off`
    - Turn on `Virtual Machine Platform` and `Windows Subsystem for Linux`
    - Confirm and reboot as prompted
    - [Open Microsoft Store, search for and install Ubuntu](https://www.microsoft.com/store/productid/9PDXGNCFSCZV?ocid=pdpshare)
    - Open `Ubuntu` from the windows app launcher when complete
    - If it fails, download and install the [x64 machine patch](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi) (Typically happens on Win11)
    - Wait for install and enter desired username as password when prompted
- Close all windows and open Command Prompt as admin
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
    - `cmake -DBUILD_SHARED_LIBS=ON ..` (Might have to hit enter if it seems to have stalled)
    - `make`
    - `sudo make install`
    - `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib`
    - `export DISPLAY=:0`
    - Edit `/home/$USER/raylib/src/Makefile`
        - Update `EMSDK_PATH` to be `/home/$(USER)/emsdk`
- Clone this repo
    - `cd ~`
    - `git clone https://github.com/bradmartin333/WSL2RaylibWASM.git`
    - `cd WSL2RaylibWASM`
- Build `main.cpp` executable named `test`
    -  `g++ main.cpp -lraylib -o test`
- Build `main.cpp` for wasm
    - `cd ~/WSL2RaylibWASM`
    - `./wasm_build.sh`
        - Take a look at file to understand what is happening
    - Open `build/game.html` in a live server
        - `python -m http.server 8000`
