echo "adding asdf python plugin"
asdf plugin add python
echo "done"

echo "installing python"
asdf install python latest
echo "done"

echo "set latest version to system wide version"
asdf global python latest
echo "done"

echo "installing pipenv"
brew install pipenv
echo "done"

echo "installing Black"
pipenv install black
echo "done"

echo "installing numpy"
pipenv install numpy
echo "done"