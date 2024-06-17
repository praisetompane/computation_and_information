echo "adding asdf language plugin"
    asdf plugin add language
echo "done"

echo "installing language"
    asdf install language latest
echo "done"

echo "set latest version to system wide version"
    asdf global language latest
echo "done"

echo "adding asdf package manager plugin"
    asdf plugin add package manager
echo "done"

echo "installing package manager"
    asdf install package manager latest
    pnpm setup
echo "done"

echo "set latest version to system wide version"
    asdf global package manager latest
echo "done"
