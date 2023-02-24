echo "adding asdf scala plugin"
asdf plugin add scala
echo "done"

echo "installing scala"
asdf install scala latest
echo "done"

echo "set latest version to system wide version"
asdf global scala latest
echo "done"

echo "adding asdf sbt plugin"
asdf plugin add sbt
echo "done"

echo "installing sbt"
asdf install sbt latest
echo "done"

echo "set latest version to system wide version"
asdf global sbt latest
echo "done"
