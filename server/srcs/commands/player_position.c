/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	player_position(server_t *server, client_t *client, char *str)
{
	int	id;
	
	while (*str && *str != '#')
		str++;
	if (*str == '#')
		str++;
	else {
		printf("error player position\n");
		return ;
	}
	id = atoi(str);
	for (int i = 0; server->clients[i] != NULL; i++){
		if (server->clients[i]->id == id)
			dprintf(client->fd, "ppo %d %d %d\n",
			id, server->clients[i]->posX,
			server->clients[i]->posY);
	}
}