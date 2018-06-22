/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	forwardY(server_t *server, client_t *client)
{
	if (client->orientation == 3) {
		if (client->pos_y == server->parse->height - 1)
			client->pos_y = 0;
		else
			client->pos_y++;
	}
	if (client->orientation == 4) {
		if (client->pos_x == 0)
			client->pos_x = server->parse->width - 1;
		else
			client->pos_x++;
	}
	return (OK);
}

int	forward(server_t *server, client_t *client, char *str)
{
	str = str;

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
	append_player(&server->map[client->pos_y][client->pos_x], client);
	dprintf(client->fd, "ok\n");
	return (OK);
}

int	right(server_t *server, client_t *client, char *str)
{
	(void)str;
	(void)server;
	switch (client->orientation) {
		case 1:
			client->orientation = 2;
			break ;
		case 2:
			client->orientation = 3;
			break ;
		case 3:
			client->orientation = 4;
			break ;
		case 4:
			client->orientation = 1;
			break ;
	}
	dprintf(client->fd, "ok\n");
	return (OK);
}

int	left(server_t *server, client_t *client, char *str)
{
	(void)str;
	(void)server;
	switch(client->orientation) {
		case 1:
			client->orientation = 4;
			break;
		case 2:
			client->orientation = 1;
			break;
		case 3:
			client->orientation = 2;
			break;
		case 4:
			client->orientation = 3;
			break;
	}
	dprintf(client->fd, "ok\n");
	return (OK);
}
