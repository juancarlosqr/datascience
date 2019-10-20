# Docker

## General

__List CLI commands__

```
docker
docker COMMAND --help
```

__Display version and info__

```
docker -v
# info about your Docker Client and Server versions
docker version
docker info
```

__Prune system__

Delete all unused containers, unused networks, and dangling images

```
docker system prune
docker system prune --all --force --volumes
```

__Inspect__

Return low-level information on Docker objects

```
docker inspect name|id
```

## Containers

__List__

```
# running
docker ps
docker container ls

# all
docker ps -a
docker container ls --all

# all in quiet mode
docker ps -aq
docker container ls -aq

# size
docker ps -s

# filter
docker ps --filter "name=nostalgic"
```

__Create__

```
docker create
```

__Start__

```
docker container start CONTAINER_ID
docker start CONTAINER_ID
```

__Stop__

```
docker container stop CONTAINER_ID
docker stop CONTAINER_ID

# stop all running containers
docker container stop $(docker container ps -q)
```

__Kill__

```
docker container kill CONTAINER_ID
docker kill CONTAINER_ID
```

__Remove__

```
docker container rm CONTAINER_ID
docker rm CONTAINER_ID
docker container rm $(docker container ps -aq)

# filter containers of rabbitmq
docker container rm $(docker ps -a | grep rabbitmq | awk '{print $1}')

# filter by time created
docker container rm $(docker ps -a | grep "46 hours ago")
```

__Exec__

```
# run a command in a running container
docker container exec -it CONTAINER_ID bash
```

__Attach__

```
docker container attach CONTAINER_ID
docker attach CONTAINER_ID
```

__Logs__

```
docker container logs CONTAINER_ID
docker logs CONTAINER_ID
```

__Top__

```
docker container top CONTAINER_ID
docker top CONTAINER_ID
```

__Stats__

```
docker container stats CONTAINER_ID
docker stats CONTAINER_ID
```

## Images

__List__

```
docker image ls
docker images

# all
docker images -a

# quiet mode
docker images -q

# filter
docker images --filter "dangling=true"
```

__Run__

```
docker run TAG

# map ports
docker run -p 8000:80 TAG

# --rm remove container when exiting
docker run --rm TAG

# -d for detached mode - run in background
docker run -d --rm -p 8000:80 TAG
```

__Build__

```
docker build -t image:tag .
docker build --tag image:tag .
```

__Remove__

```
docker image rm [IMAGE ID]
docker rmi [IMAGE ID]
docker image rm $(docker image ls -q)
```

__Tag__

```
docker tag image username/repository:tag
```

__Push__

```
docker push username/repository:tag
```

__Pull__

```
docker pull username/repository:tag
```

__History__

Show the history of an image. Useful to see the size of the intermediate images that make up your image

```
docker history my_image:tag
```

## Networks

__List__

```
docker network ls
```

__Prune__

```
docker network prune
```

__Remove__

```
docker network rm [NETWORK]
```

## Basics

```
docker build -t friendlyhello .  # Create image using this directory's Dockerfile
docker run -p 4000:80 friendlyhello  # Run "friendlyname" mapping port 4000 to 80
docker run -d -p 4000:80 friendlyhello         # Same thing, but in detached mode
docker container ls                                # List all running containers
docker container ls -a             # List all containers, even those not running
docker container stop <hash>           # Gracefully stop the specified container
docker container kill <hash>         # Force shutdown of the specified container
docker container rm <hash>        # Remove specified container from this machine
docker container rm $(docker container ls -a -q)         # Remove all containers
docker image ls -a                             # List all images on this machine
docker image rm <image id>            # Remove specified image from this machine
docker image rm $(docker image ls -a -q)   # Remove all images from this machine
docker login             # Log in this CLI session using your Docker credentials
docker tag <image> username/repository:tag  # Tag <image> for upload to registry
docker push username/repository:tag            # Upload tagged image to registry
docker run username/repository:tag                   # Run image from a registry
```

## Concepts

- The Docker image is created at build time and the Docker container is created at run time
- A container is built from a series of layers. Each layer is read only, except the final container layer that sits on top of the others

## Diagram

![Diagram](https://cdn-images-1.medium.com/max/1600/0*rgvX6TzfW4HqNpiQ)

## Ecosystem

__Basics__

- Platform - the software that makes Docker containers possible
- Engine - client-server app (CE or Enterprise)
- Client - handles Docker CLI so you can communicate with the Daemon
- Daemon - Docker server that manages key things
- Volumes - persistent data storage
- Repository - collection of Docker images, e.g. Alpine
- Registry - remote image storage
- Docker Hub - default and largest Docker Registry

_A registry is a collection of repositories, and a repository is a collection of images_

__Scaling__

> Generally the containers in an application built using Docker Compose will all run on the same host. Managing containers running on different hosts usually requires an additional tool, such as Docker Swarm or Kubernetes

- Networking - connect containers together
- Compose - time saver for multi-container apps
- Swarm - orchestrates container deployment (but use Kubernetes instead)
- Services - containers in production
- Kubernetes - automates deployment, scaling, and management of containerized applications

## Dockerfile

_Only the instructions FROM, RUN, COPY, and ADD create layers in the final image. Other instructions configure things_

- `FROM` specifies the base (parent) image.
- `LABEL` provides metadata. Good place to include maintainer info.
- `ENV` sets a persistent environment variable.
- `RUN` runs a command and creates an image layer. Used to install packages into containers.
- `COPY` copies files and directories to the container.
- `ADD` copies files and directories to the container. Can upack local .tar files.
- `CMD` provides a command and arguments for an executing container. Parameters can be overridden. There can be only one CMD.
- `WORKDIR` sets the working directory for the instructions that follow.
- `ARG` defines a variable to pass to Docker at build-time.
- `ENTRYPOINT` provides command and arguments for an executing container. Arguments persist. 
- `EXPOSE` exposes a port.
- `VOLUME` creates a directory mount point to access and store persistent data.

__Resources__

- [best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [cheat sheet](https://kapeli.com/cheat_sheets/Dockerfile.docset/Contents/Resources/Documents/index)

__Best practices__

[Eight Best Practices to Reduce Image Sizes & Build Times](https://towardsdatascience.com/slimming-down-your-docker-images-275f0ca9337e)

1. Use an official base image whenever possible. Official images are updated regularly and are more secure than un-official images.
2. Use variations of `Alpine` images when possible to keep your images lightweight.
3. If using `apt`, combine `RUN apt-get update` with `apt-get install` in the same instruction. Then chain multiple packages in that instruction. List the packages in alphabetical order over multiple lines with the `\` character. For example:

```sh
RUN apt-get update && apt-get install -y \
    package-one \
    package-two \
    package-three
 && rm -rf /var/lib/apt/lists/*
 ```

This method reduces the number of layers to be built and keeps things nice and tidy. 

4. Include `&& rm -rf /var/lib/apt/lists/*` at the end of the `RUN` instruction to clean up the apt cache so it isn’t stored in the layer.
5. Use caching wisely by putting instructions likely to change lower in your Dockerfile.
6. Use a `.dockerignore` file to keep unwanted and unnecessary files out of your image. [read here](https://docs.docker.com/engine/reference/builder/#dockerignore-file).
7. Check out [dive](https://github.com/wagoodman/dive) - a very cool tool for inspecting your Docker image layers and helping you trim the fat. 
8. Don’t install packages you don’t need. Duh! But common.

__Cache__

- [read here](https://towardsdatascience.com/slimming-down-your-docker-images-275f0ca9337e)

```
# To avoid cache issues
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/
```

__Multistage Builds__

- [read here](https://towardsdatascience.com/slimming-down-your-docker-images-275f0ca9337e)
