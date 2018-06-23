/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	eject(server_t *server, client_t *client, char *str)
{
	int clients = 0;
	client_t *tmp;
	tile_t	*tile = server->map[client->pos_y][client->pos_x];

	(void)str;
	for (; tile->clients[clients]; clients++);
	if (clients == 1)
		dprintf(client->fd, "ko\n");
	else
		dprintf(client->fd, "ok\n");
	for (int i = 0; i < clients;) {
		if (tile->clients[i] != client) {
			tmp = tile->clients[i];
			push_client(server, tmp, client->orientation);
			clients--;
		}
		else
			i++;
	}
	return (OK);
}
