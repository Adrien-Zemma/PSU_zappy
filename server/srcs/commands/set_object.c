/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	set_other_other(server_t *server, client_t *client, char *str)
{
	if (strcmp("phiras", str) == 0){
		if (client->phiras != 0) {
			client->phiras--;
			server->map[client->posY][client->posX]->phiras++;
		}
	}
	else if (strcmp("thystame", str) == 0) {
		if (client->thystame != 0) {
			client->thystame--;
			server->map[client->posY][client->posX]->thystam++;
		}
	}
	for (int i = 0; server->clients[i] != NULL; i++)
		if (server->clients[i]->id == -1)
			dprintf(server->clients[i]->fd, "pdr %d 1\n", client->fd);
	dprintf(client->fd, "ok\n");
	return OK;
}

int	set_other_object(server_t *server, client_t *client, char *str)
{
	if (strcmp("deraumere", str) == 0){
		if (client->demaumere != 0){
			client->demaumere--;
			server->map[client->posY][client->posX]->deraumere++;
		}
	}
	else if (strcmp("sibur", str) == 0) {
		if (client->sibur != 0) {
			client->sibur--;
			server->map[client->posY][client->posX]->sibur++;
		}
	}
	else if (strcmp("mendiane", str) == 0){
		if (client->mendiane != 0) {
			client->mendiane--;
			server->map[client->posY][client->posX]->mendiane++;
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
		return BAD_PARAM;
	if (strcmp("linemate", str) == 0){
		if (client->linemate != 0) {
			client->linemate--;
			server->map[client->posY][client->posX]->linemate++;
		}
	}
	else if (strcmp("food", str) == 0){
		if (client->food != 0) {
			client->food--;
			server->map[client->posY][client->posX]->food++;
		}
	}
	return (set_other_object(server, client, str));
}

