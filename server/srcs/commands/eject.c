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
		if (client->pos_y == 0)
			client->pos_y = server->parse->height - 1;
		else
			client->pos_y--;
	}
	if (client->orientation == 2) {
		if (client->pos_x == server->parse->width - 1)
			client->pos_x = 0;
		else
			client->pos_x++;
	}
	forwardY(server, client);
}

int	eject(server_t *server, client_t *client, char *str)
{
	int clients;

	(void)str;
	for (clients = 0; server->map[client->pos_y][client->pos_x]->clients[clients]; clients++);
	if (clients == 1) {
		dprintf(client->fd, "ko\n");
		return (KO);
	}
	for (int i = 0; i < clients;) {
		if (server->map[client->pos_y][client->pos_x]->clients[i] != client) {
			server->map[client->pos_y][client->pos_x]->clients[i]->orientation = client->orientation;
			push_somebody(server, server->map[client->pos_y][client->pos_x]->clients[i]);
			clients--;
		}
		else
			i++;
	}
	dprintf(client->fd, "ok\n");
	return (OK);
}
