/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

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
	printf("add a new connect %d\n", server->nb_fd);
	return (0);	
}