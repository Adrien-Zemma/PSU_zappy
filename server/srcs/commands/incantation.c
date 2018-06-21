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
	int i;

	for (i = 0; tile->clients[i]; i++);
	if (tile->linemate >= level.linemate &&
	tile->deraumere >= level.deraumere &&
	tile->sibur >= level.sibur &&
	tile->mendiane >= level.mendiane &&
	tile->phiras >= level.phiras &&
	i >= level.minPlayers)
		return (1);
	return (0);
}

static void	remove_minerals(tile_t **p_tile, tile_t level)
{
	printf("%d|%d\n", (*p_tile)->linemate, level.linemate);
	printf("%d|%d\n", (*p_tile)->deraumere, level.deraumere);
	printf("%d|%d\n", (*p_tile)->sibur, level.sibur);
	printf("%d|%d\n", (*p_tile)->mendiane, level.mendiane);
	printf("%d|%d\n", (*p_tile)->phiras, level.phiras);
	printf("%d|%d\n", (*p_tile)->thystam, level.thystam);
	(*p_tile)->linemate -= level.linemate;
	(*p_tile)->deraumere -= level.deraumere;
	(*p_tile)->sibur -= level.sibur;
	(*p_tile)->mendiane -= level.mendiane;
	(*p_tile)->phiras -= level.phiras;
	(*p_tile)->thystam -= level.thystam;
}

int	start_incantation(server_t *server, client_t *client, char *str)
{
	draw_tile(server->map, 1, client->posY, client->posX);
	if (client->level >= 8 || compare_tile_incantation(server->map[client->posY][client->posX], level_requirement[client->level - 1]) == 0)
		return KO;
	remove_minerals(&server->map[client->posY][client->posX], level_requirement[client->level - 1]);
	draw_tile(server->map, 1, client->posY, client->posX);
	return OK;
}