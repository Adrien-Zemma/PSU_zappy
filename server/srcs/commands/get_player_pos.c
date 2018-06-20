/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	get_player_pos(server_t *server, client_t *client, char *str)
{
	int client_id = -1;
	client_t	*c;

	while (*str && *str != ' ')
		str++;
	if (*str == ' ')
		str++;
	else
		return BAD_PARAM;
	client_id = atoi(str);
	if (client_id == 0)
		return KO;
	for (int i = 0; server->clients[i]; i++) {
		printf("Client:%d|%d\n", client_id, server->clients[i]->id);
		if (server->clients[i]->id == client_id) {
			c = server->clients[i];
			dprintf(client->fd, "ppo %d %d %d %d\n",
			client_id, c->posX, c->posY,
			c->orientation);
		}
	}
	return OK;
}