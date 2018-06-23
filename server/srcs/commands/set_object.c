/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

static int	send_pdr(server_t *server, client_t *client)
{
	for (int i = 0; server->clients[i] != NULL; i++)
		if (server->clients[i]->id == -1)
			dprintf(server->clients[i]->fd, "pdr %d 1\n",
				client->fd);
	return (OK);
}

int	set_other_other(server_t *server, client_t *client, char *str)
{
	if (strcmp("phiras", str) == 0) {
		if (client->phiras != 0) {
			client->phiras--;
			server->map[client->pos_y][client->pos_x]->phiras++;
			dprintf(client->fd, "ok\n");
			return (send_pdr(server, client));
		}
	}
	else if (strcmp("thystame", str) == 0) {
		if (client->thystame != 0) {
			client->thystame--;
			server->map[client->pos_y][client->pos_x]->thystam++;
			dprintf(client->fd, "ok\n");
			return (send_pdr(server, client));
		}
	}
	dprintf(client->fd, "ko\n");
	return (OK);
}

int	set_other_object(server_t *server, client_t *client, char *str)
{
	if (strcmp("deraumere", str) == 0) {
		if (client->demaumere != 0) {
			client->demaumere--;
			server->map[client->pos_y][client->pos_x]->deraumere++;
			dprintf(client->fd, "ok\n");
			return (send_pdr(server, client));
		}
	}
	else if (strcmp("sibur", str) == 0) {
		if (client->sibur != 0) {
			client->sibur--;
			server->map[client->pos_y][client->pos_x]->sibur++;
			dprintf(client->fd, "ok\n");
			return (send_pdr(server, client));
		}
	}
	else if (strcmp("mendiane", str) == 0) {
		if (client->mendiane != 0) {
			client->mendiane--;
			server->map[client->pos_y][client->pos_x]->mendiane++;
			dprintf(client->fd, "ok\n");
			return (send_pdr(server, client));
		}
	}
	return (set_other_other(server, client, str));
}

int	set_object(server_t *server, client_t *client, char *str)
{
	while (*str && *str != ' ')
		str++;
	if (*str == ' ')
		str++;
	else
		return (BAD_PARAM);
	if (strcmp("linemate", str) == 0) {
		if (client->linemate != 0) {
			client->linemate--;
			server->map[client->pos_y][client->pos_x]->linemate++;
			dprintf(client->fd, "ok\n");
			return (send_pdr(server, client));
		}
	}
	else if (strcmp("food", str) == 0) {
		if (client->food != 0) {
			client->food--;
			server->map[client->pos_y][client->pos_x]->food++;
			dprintf(client->fd, "ok\n");
			return (send_pdr(server, client));
		}
	}
	return (set_other_object(server, client, str));
}
