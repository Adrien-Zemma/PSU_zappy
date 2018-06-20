/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	take_other_other(server_t *server, client_t *client, char *str)
{
	if (strcmp("phiras", str) == 0){
		if (server->map[client->posY][client->posX]->phiras != 0) {
			server->map[client->posY][client->posX]->phiras--;
			client->phiras++;
		}
	}
	else if (strcmp("thystame", str) == 0){
		if (server->map[client->posY][client->posX] != 0){
			server->map[client->posY][client->posX]->thystam--;
			client->thystame++;
		}
	}
	for (int i = 0; server->clients[i] != NULL; i++)
		if (server->clients[i]->id == -1)
			dprintf(server->clients[i]->fd, "pgt %d 1\n", client->fd);
	return OK;
}

int	take_other_object(server_t *server, client_t *client, char *str)
{
	if (strcmp("deraumere", str) == 0){
		if (server->map[client->posY][client->posX]->deraumere != 0) {
			server->map[client->posY][client->posX]->deraumere--;
			client->demaumere++;
		}
	}
	else if (strcmp("sibur", str) == 0){
		if (server->map[client->posY][client->posX]->sibur != 0) {
			server->map[client->posY][client->posX]->sibur--;
			client->sibur++;
		}
	}
	else if (strcmp("mendiane", str) == 0){
		if (server->map[client->posY][client->posX]->mendiane != 0) {
			server->map[client->posY][client->posX]->mendiane--;
			client->mendiane++;
		}
	}
	return (take_other_other(server, client, str));
}


int	take_object(server_t *server, client_t *client, char *str)
{
	while (*str && *str != ' ')
		str++;
	if (*str == ' ')
		str++;
	else
		return BAD_PARAM;
	if (strcmp("linemate", str) == 0){
		if (server->map[client->posY][client->posX]->linemate != 0) {
			server->map[client->posY][client->posX]->linemate--;
			client->linemate++;
		}
	}
	else if (strcmp("food", str) == 0){
		if (server->map[client->posY][client->posX]->food != 0) {
			server->map[client->posY][client->posX]->food--;
			client->food++;
		}
	}
	return (take_other_object(server, client, str));
}
