echo "Starting..."
# definimos variables.
IMAGE_NAME="rest-api-ml"
CONTAINER_NAME="$IMAGE_NAME-con"

echo $IMAGE_NAME
echo $CONTAINER_NAME

echo "Stoping container $CONTAINER_NAME"
if docker stop $CONTAINER_NAME 2>&1 | grep -q "No such"; then
  echo "Error trying stop container $CONTAINER_NAME maybe container does not exist"
else
  echo "$CONTAINER_NAME has been stopped. Good job!"
fi

echo "Removing container $CONTAINER_NAME"
if docker rm $CONTAINER_NAME 2>&1 | grep -q "No such"; then
  echo "Error trying remove container $CONTAINER_NAME maybe container does not exist"
else
  echo "$CONTAINER_NAME has been removed. Good job!"
fi

echo "Removing image $IMAGE_NAME"
if docker rmi $IMAGE_NAME 2>&1 | grep -q "No such"; then
  echo "Error trying remove image $IMAGE_NAME maybe image does not exist"
else
  echo "$IMAGE_NAME has been removed. Good job!"
fi

docker build --tag $IMAGE_NAME .