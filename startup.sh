
#export LD_LIBRARY_PATH=$(nix eval --raw nixpkgs.xorg.libXrender)/lib:$LD_LIBRARY_PATH
#export LD_LIBRARY_PATH=$(nix eval --raw nixpkgs.xorg.libXext)/lib:$LD_LIBRARY_PATH
#export PYTHON_LD_LIBRARY_PATH=$(nix eval --raw nixpkgs.xorg.libXext)/lib:$PYTHON_LD_LIBRARY_PATH
#export PYTHON_LD_LIBRARY_PATH=$(nix eval --raw nixpkgs.xorg.libXext)/lib:$PYTHON_LD_LIBRARY_PATH
source .bashrc
echo $LD_LIBRARY_PATH
