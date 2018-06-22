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

static int	compare_tile_incantation(tile_t *tile, tile_t level)
{
	int id = 0;

	for (int i = 0; tile->clients[i]; i++)
		id += (tile->clients[i]->is_incanting == 1 ? 1 : 0);
	if (tile->linemate >= level.linemate &&
	tile->deraumere >= level.deraumere &&
	tile->sibur >= level.sibur &&
	tile->mendiane >= level.mendiane &&
	tile->phiras >= level.phiras &&
	id + 1 >= level.minPlayers)
		return (1);
	return (0);
}

static void	remove_minerals(tile_t **p_tile, tile_t level)
{
	(*p_tile)->linemate -= level.linemate;
	(*p_tile)->deraumere -= level.deraumere;
	(*p_tile)->sibur -= level.sibur;
	(*p_tile)->mendiane -= level.mendiane;
	(*p_tile)->phiras -= level.phiras;
	(*p_tile)->thystam -= level.thystam;
}

int	start_incantation(server_t *server, client_t *client, char *str)
{
	client_t	*tmp;

	(void)str;
	if (client->level >= 8 || compare_tile_incantation(server->map[client->pos_y][client->pos_x], level_requirement[client->level - 1]) == 0) {
		dprintf(client->fd, "ko\n");
		return (KO);
	}
	client->is_incanting = 1;
	for (int i = 0; server->map[client->pos_y][client->pos_x]->clients[i]; i++) {
		tmp = server->map[client->pos_y][client->pos_x]->clients[i];
		dprintf(tmp->fd, "Elevation underway\n");
		queue_append(&tmp->command, append_command(NULL, end_incantation, 300 / (double)server->parse->freq));
	}
	return (OK);
}

int	end_incantation(server_t *server, client_t *client, char *str)
{
	(void)str;
	remove_minerals(&server->map[client->pos_y][client->pos_x], level_requirement[client->level - 1]);
	client->level++;
	dprintf(client->fd, "Current level: %d\n", client->level);
	client->is_incanting = 0;
	return (0);
}
