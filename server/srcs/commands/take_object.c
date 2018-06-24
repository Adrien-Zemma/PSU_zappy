/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

static int	send_pgt(server_t *server, client_t *client)
{
	add_if_empty(server->map);
	for (int i = 0; server->clients[i] != NULL; i++)
		if (server->clients[i]->id == -1)
			dprintf(server->clients[i]->fd, "pgt %d 1\n",
				client->fd);
	return (OK);
}

int	take_other_other(server_t *server, client_t *client, char *str)
{
	if (strcmp("phiras", str) == 0) {
		if (server->map[client->pos_y][client->pos_x]->phiras != 0) {
			server->map[client->pos_y][client->pos_x]->phiras--;
			client->phiras++;
			dprintf(client->fd, "ok\n");
			return (send_pgt(server, client));
		}
	}
	else if (strcmp("thystame", str) == 0) {
		if (server->map[client->pos_y][client->pos_x] != 0) {
			server->map[client->pos_y][client->pos_x]->thystam--;
			client->thystame++;
			dprintf(client->fd, "ok\n");
			return (send_pgt(server, client));
		}
	}
	dprintf(client->fd, "ko\n");
	return (OK);
}

int	take_other_bis_object(server_t *server, client_t *client, char *str)
{
	if (strcmp("sibur", str) == 0) {
		if (server->map[client->pos_y][client->pos_x]->sibur != 0) {
			server->map[client->pos_y][client->pos_x]->sibur--;
			client->sibur++;
			dprintf(client->fd, "ok\n");
			return (send_pgt(server, client));
		}
	}
	else if (strcmp("mendiane", str) == 0) {
		if (server->map[client->pos_y][client->pos_x]->mendiane != 0) {
			server->map[client->pos_y][client->pos_x]->mendiane--;
			client->mendiane++;
			dprintf(client->fd, "ok\n");
			return (send_pgt(server, client));
		}
	}
	return (take_other_other(server, client, str));
}

int	take_other_object(server_t *server, client_t *client, char *str)
{
	if (strcmp("food", str) == 0){
		if (server->map[client->pos_y][client->pos_x]->food != 0) {
			server->map[client->pos_y][client->pos_x]->food--;
			client->food++;
			dprintf(client->fd, "ok\n");
			return (send_pgt(server, client));
		}
	}
	else if (strcmp("deraumere", str) == 0) {
		if (server->map[client->pos_y][client->pos_x]->deraumere != 0) {
			server->map[client->pos_y][client->pos_x]->deraumere--;
			client->demaumere++;
			dprintf(client->fd, "ok\n");
			return (send_pgt(server, client));
		}
	}
	return (take_other_bis_object(server, client, str));
}


int	take_object(server_t *server, client_t *client, char *str)
{
	while (*str && *str != ' ')
		str++;
	if (*str == ' ')
		str++;
	else
		return (BAD_PARAM);
	if (strcmp("linemate", str) == 0){
		if (server->map[client->pos_y][client->pos_x]->linemate != 0) {
			server->map[client->pos_y][client->pos_x]->linemate--;
			client->linemate++;
			dprintf(client->fd, "ok\n");
			return (send_pgt(server, client));
		}
	}
	return (take_other_object(server, client, str));
}
