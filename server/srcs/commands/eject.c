/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	push_somebody(server_t *server, client_t *client)
{
	remove_player(server->map, client);
	if (client->orientation == 1) {
		if (client->posY == 0)
			client->posY = server->parse->height - 1;
		else
			client->posY--;
	}
	if (client->orientation == 2) {
		if (client->posX == server->parse->width - 1)
			client->posX = 0;
		else
			client->posX++;
	}
	forwardY(server, client);
}

int	eject(server_t *server, client_t *client, char *str)
{
	int clients;

	(void)str;
	for (clients = 0; server->map[client->posY][client->posX]->clients[clients]; clients++);
	if (clients == 1) {
		dprintf(client->fd, "ko\n");
		return (KO);
	}
	for (int i = 0; i < clients;) {
		if (server->map[client->posY][client->posX]->clients[i] != client) {
			server->map[client->posY][client->posX]->clients[i]->orientation = client->orientation;
			push_somebody(server, server->map[client->posY][client->posX]->clients[i]);
			clients--;
		}
		else
			i++;
	}
	dprintf(client->fd, "ok\n");
	return (OK);
}
