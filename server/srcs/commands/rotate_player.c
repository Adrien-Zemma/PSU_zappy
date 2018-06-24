/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	push_client(server_t *server, client_t *client, size_t orientation)
{
	remove_player(server->map, client);
	if (orientation == 1)
		client->pos_y = map_val_pos(server->parse->height,
						client->pos_y - 1);
	else if (orientation == 2)
		client->pos_x = map_val_pos(server->parse->width,
						client->pos_x + 1);
	if (orientation == 3)
		client->pos_y = map_val_pos(server->parse->height,
						client->pos_y + 1);
	else if (orientation == 4)
		client->pos_x = map_val_pos(server->parse->width,
						client->pos_x - 1);
	append_player(&server->map[client->pos_y][client->pos_x], client);
	return (OK);
}

int	forward(server_t *server, client_t *client, char *str)
{
	(void) str;
	push_client(server, client, client->orientation);
	dprintf(client->fd, "ok\n");
	return (OK);
}

int	right(server_t *server, client_t *client, char *str)
{
	(void)str;
	(void)server;
	client->orientation = map_val_pos(4, client->orientation + 1 - 1) + 1;
	dprintf(client->fd, "ok\n");
	return (OK);
}

int	left(server_t *server, client_t *client, char *str)
{
	(void)str;
	(void)server;
	client->orientation = map_val_pos(4, client->orientation - 1 - 1) + 1;
	dprintf(client->fd, "ok\n");
	return (OK);
}
