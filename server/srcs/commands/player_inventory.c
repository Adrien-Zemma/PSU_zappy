/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	player_inventory(server_t *server, client_t *client, char *str)
{
	int	id;
	
	while (*str && *str != '#')
		str++;
	if (*str == '#')
		str++;
	else {
		printf("error inventory player\n");
		return BAD_PARAM;
	}
	id = atoi(str);
	for (int i = 0; server->clients[i] != NULL; i++){
		if (server->clients[i]->id == id)
			dprintf(client->fd, "pin %d %d %d %d %d %d %d %d %d %d\n",
			id, server->clients[i]->posX, server->clients[i]->posY,
			server->clients[i]->food, server->clients[i]->linemate,
			server->clients[i]->demaumere, server->clients[i]->sibur,
			server->clients[i]->mendiane, server->clients[i]->phiras,
			server->clients[i]->thystame);
	}
	return OK;
}