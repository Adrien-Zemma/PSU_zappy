/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"
#include "commands.h"

const tile_t level_requirement[] = {
	{1, 1, 0, 0, 0, 0, 0, 0, NULL},
	{2, 1, 1, 1, 0, 0, 0, 0, NULL},
	{2, 2, 0, 1, 0, 2, 0, 0, NULL},
	{4, 1, 1, 2, 0, 1, 0, 0, NULL},
	{4, 1, 2, 1, 3, 0, 0, 0, NULL},
	{6, 1, 2, 3, 0, 1, 0, 0, NULL},
	{6, 2, 2, 2, 2, 2, 1, 0, NULL},
};

static int	compare_tile_incantation(client_t *origin,
					tile_t *tile,
					const tile_t *level)
{
	int id = 0;

	for (int i = 0; tile->clients[i]; i++) {
		if (tile->clients[i]->level != origin->level)
			return (0);
		id += (tile->clients[i]->is_incanting == 1 ? 1 : 0);
	}
	if (tile->linemate >= level->linemate &&
	tile->deraumere >= level->deraumere &&
	tile->sibur >= level->sibur &&
	tile->mendiane >= level->mendiane &&
	tile->phiras >= level->phiras &&
	id + 1 >= level->minPlayers)
		return (1);
	return (0);
}

void	remove_minerals(tile_t **p_tile, const tile_t *level)
{
	(*p_tile)->linemate -= level->linemate;
	(*p_tile)->deraumere -= level->deraumere;
	(*p_tile)->sibur -= level->sibur;
	(*p_tile)->mendiane -= level->mendiane;
	(*p_tile)->phiras -= level->phiras;
	(*p_tile)->thystam -= level->thystam;
}

int	start_incantation(server_t *server, client_t *client, char *str)
{
	tile_t	*tile = server->map[client->pos_y][client->pos_x];

	(void)str;
	if (client->level >= 8
	|| compare_tile_incantation(client, tile,
				&level_requirement[client->level - 1]) == 0) {
		dprintf(client->fd, "ko\n");
		queue_append(&client->command,
			append_command(NULL,
			end_incantation,
			300 / (double)server->parse->freq));
		return (KO);
	}
	client->is_incanting = 1;
	for (int i = 0; tile->clients[i]; i++) {
		dprintf(tile->clients[i]->fd, "Elevation underway\n");
		if (tile->clients[i] == client)
			queue_append(&client->command,
				append_command(NULL,
				end_incantation,
				300 / (double)server->parse->freq));
		else
			queue_append(&tile->clients[i]->command,
				append_command(NULL,
				block, 300 / (double)server->parse->freq));
	}
	return (OK);
}

int	end_incantation(server_t *server, client_t *client, char *str)
{
	int	st = 0;
	tile_t	*tile = server->map[client->pos_y][client->pos_x];
	client_t **clients = tile->clients;

	(void)str;
	if (compare_tile_incantation(client, tile,
				&level_requirement[client->level - 1]) == 0) {
		dprintf(client->fd, "ko\n");
		st = 1;
		remove_minerals(&tile, &level_requirement[client->level - 1]);
	}
	else
		for (int i = 0; clients[i]; i++)
			clients[i]->level++;
	for (int i = 0; clients[i]; i++) {
		if (clients[i] != client || !st)
			dprintf(clients[i]->fd, "Current level: %d\n",
				client->level);
		clients[i]->is_incanting = 0;
	}
	return (0);
}
