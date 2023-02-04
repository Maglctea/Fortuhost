import docker

client = docker.from_env()


def get_status(id_container):
    """
    :param id_container:
    :return: int status
    1 - exited
    2 - running
    3 - restarting
    """
    container = client.containers.get(str(id_container))

    status = container.status
    if status == 'exited':
        return 1
    elif status == 'running':
        return 2
    elif status == 'restarting':
        return 3
    else:
        return -1


def add_app(id_app):
    image = client.images.build(path=f'app/docker_task/{id_app}/', tag=str(id_app), rm=True)
    container = client.containers.run(image=image[0], stream=True, name=str(id_app), detach=True)
    return container


def stop_app(id_app):
    container = client.containers.get(str(id_app))
    container.stop(timeout=5)
    return container


def start_app(id_app):
    container = client.containers.get(str(id_app))
    container.start()
    return container


def restart_app(id_app):
    container = client.containers.get(str(id_app))
    container.restart(timeout=5)
    return container


def delete_app(id_app):
    container = client.containers.get(str(id_app))
    container.remove(force=True)
    image = client.images.get(str(id_app))
    image.remove(force=True)

