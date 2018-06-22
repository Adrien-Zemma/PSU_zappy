/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	player_level(server_t *server, client_t *client, char *str)
{
	int	id;

	while (*str && *str != '#')
		str++;
	if (*str == '#')
		str++;
	else{
		printf("Error level player\n");
		return BAD_PARAM;
	}
	id = atoi(str);
	for (int i = 0; server->clients[i] != NULL; i++){
		if (server->clients[i]->id == id)
			dprintf(client->fd,
				"plv %d %d", id, server->clients[i]->level);
	}
	dprintf(client->fd, "\n");
	return OK;
}

int	forke(server_t *server, client_t *client, char *str)
{
	str = str;
	for (int i = 0; server->clients[i] != NULL; i++) {
		if (server->clients[i]->id == -1)
			dprintf(server->clients[i]->fd, "pfk %d\n", client->id);
	}
	dprintf(client->fd, "ok\n");
	return (0);
}

int	gtp(server_t *server, client_t *client, char *str)
{
	int	id;

	while (*str && *str != '#')
		str++;
	if (*str == '#')
		str++;
	else
		return (1);
	id = atoi(str);
	for (int i = 0; server->clients[i] != NULL; i++) {
		if (server->clients[i]->id == id)
			dprintf(client->fd, "%s\n", server->clients[i]->team);
	}
	return (0);
}

int	gai(server_t *server, client_t *client, char *str)
{
	str = str;
	dprintf(client->fd, "gai");
	for (int i = 0; server->clients[i] != NULL; i++) {
		if (server->clients[i]->id != -1)
			dprintf(client->fd, " %d", server->clients[i]->id);
	}
	dprintf(client->fd, "\n");
	return 0;
}
