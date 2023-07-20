echo "installing brew"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo "done"


echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> /home/praisetompane/.profile

eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

ostype="$(uname -s)"
if [ "$ostype" = "Linux" ]; then 
    sudo apt-get install build-essential
fi

brew install gccac