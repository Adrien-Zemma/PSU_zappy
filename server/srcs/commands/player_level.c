/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	player_level(server_t *server, client_t *client, char *str)
{
	int	id;
	
	while (*str && *str != '#')
		str++;
	if (*str == '#')
		str++;
	else{
		printf("Error level player\n");
		return ;
	}
	id = atoi(str);
	for (int i = 0; server->clients[i] != NULL; i++){
		if (server->clients[i]->id == id)
			dprintf(client->fd,
				"plv %d %d", id, server->clients[i]->level);
	}
	dprintf(client->fd, "\n");
}