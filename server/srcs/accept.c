/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	set_client(server_t *server)
{
	server->clients[server->nb_client - 1]->food = 1;
	server->clients[server->nb_client - 1]->linemate = 0;
	server->clients[server->nb_client - 1]->demaumere = 0;
	server->clients[server->nb_client - 1]->sibur = 0;
	server->clients[server->nb_client - 1]->mendiane = 0;
	server->clients[server->nb_client - 1]->phiras = 0;
	server->clients[server->nb_client - 1]->thystame = 0;
	server->clients[server->nb_client - 1]->level = 1;
	server->clients[server->nb_client - 1]->id = server->nb_client;
	server->clients[server->nb_client - 1]->posX = ADD_MINERAL(0, server->parse->width);
	server->clients[server->nb_client - 1]->posY = ADD_MINERAL(0, server->parse->height);
	return (0);
}

int	set_accept(server_t *server)
{
	int	tmp;
	struct	sockaddr_in	s_sin_client;
	socklen_t	s_sin_size = sizeof(s_sin_client);
	
	tmp = accept(server->fd, (struct sockaddr *)&s_sin_client, &s_sin_size);
	if (tmp == -1)
		perror("accept :");
	server->fds[server->nb_fd] = tmp;
	server->nb_fd++;
	server->fds = realloc(server->fds, sizeof(int) * (server->nb_fd + 1));
	server->nb_client++;
	server->clients = realloc(server->clients,
		sizeof(client_t *) * (1 + server->nb_client));
	server->clients[server->nb_client - 1] = malloc(sizeof(client_t));
	server->clients[server->nb_client] = NULL;
	server->clients[server->nb_client - 1]->fd = tmp;
	return (set_client(server));
}