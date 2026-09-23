# lil_game_dev
A tiny local AP file host for web based game dev tools
current list for plan:

[ ] https://keithclark.github.io/ZzFXM/

[ ] https://killedbyapixel.github.io/ZzFX/

[ ] Mescla.capelo.me

[ ] https://github.com/pkalogiros/AudioMass/tree/production

[ ] https://github.com/piskelapp/piskel

[ ] https://github.com/cotestatnt/async-esp-fs-webserver

[ ] https://code.haverbeke.berlin/codemirror/legacy-modes/tags

[ ] Godot web version

[ ] Three.js libraries

[ ] Pixi.js libraries

[ ] https://github.com/HeyPuter/blender-wasm

[ ] Goxel web version

[ ] Etro-js/etro

[ ] Omniclip

[ ] Pixelorama

[ ] https://github.com/taniarascia/chip8

[ ] https://www.pico-8-edu.com/

[ ] strudel repl

directory structure

```
/sdcard/
├── index.html                   <-- Main Dashboard Hub (links to all tools)
├── favicon.ico
├── assets/                      <-- Shared Global Libraries
│   ├── js/
│   │   ├── three.min.js         <-- Three.js
│   │   ├── pixi.min.js          <-- Pixi.js
│   │   └── etro.min.js          <-- Etro-js audio/video composer
│   └── codemirror/              <-- CodeEditor & Legacy Syntax Modes
│       ├── codemirror.js
│       └── legacy-modes/
├── tools/                       <-- Heavy & Standalone Web Apps
│   ├── godot/                   <-- Godot Web Editor (.wasm, .pck)
│   ├── blender/                 <-- Blender Wasm build files
│   ├── pixelorama/              <-- Pixelorama sprite & animation suite
│   ├── piskel/                  <-- Piskel pixel art editor
│   ├── audiomass/               <-- AudioMass audio production suite
│   ├── goxel/                   <-- Goxel 3D voxel editor
│   ├── pico8/                   <-- PICO-8 education web wrapper
│   ├── chip8/                   <-- Chip-8 emulator / dev playground
│   ├── zzfx/                    <-- ZzFX sound effect generator
│   ├── zzfxm/                   <-- ZzFXM music tracker
│   ├── strudel/                 <-- Strudel live-coding music repl
│   └── omniclip/                <-- Omniclip media utility
└── workspace/                   <-- Your Active Game Projects
    ├── project_alpha/
    └── template_game/
```
