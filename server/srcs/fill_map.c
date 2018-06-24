/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

static void	add_tile(tile_t *first, tile_t *second)
{
	first->linemate += second->linemate;
	first->deraumere += second->deraumere;
	first->sibur += second->sibur;
	first->mendiane += second->mendiane;
	first->phiras += second->phiras;
	first->thystam += second->thystam;
	first->food += second->food;
}

static void	add_map(server_t *s, tile_t ***map, int id)
{
	map[ADD_MINERAL(0, s->parse->height)][ADD_MINERAL(0, s->parse->width)]
	->food += (id == 0 ? 1 : 0);
	map[ADD_MINERAL(0, s->parse->height)][ADD_MINERAL(0, s->parse->width)]
	->linemate += (id == 1 ? 1 : 0);
	map[ADD_MINERAL(0, s->parse->height)][ADD_MINERAL(0, s->parse->width)]
	->deraumere += (id == 2 ? 1 : 0);
	map[ADD_MINERAL(0, s->parse->height)][ADD_MINERAL(0, s->parse->width)]
	->sibur += (id == 3 ? 1 : 0);
	map[ADD_MINERAL(0, s->parse->height)][ADD_MINERAL(0, s->parse->width)]
	->mendiane += (id == 4 ? 1 : 0);
	map[ADD_MINERAL(0, s->parse->height)][ADD_MINERAL(0, s->parse->width)]
	->phiras += (id == 5 ? 1 : 0);
	map[ADD_MINERAL(0, s->parse->height)][ADD_MINERAL(0, s->parse->width)]
	->thystam += (id == 6 ? 1 : 0);
}

void	add_if_empty(server_t *serv, tile_t ***map)
{
	tile_t	stock = {0, 0, 0, 0, 0, 0, 0, 0, NULL};
	int	max = (serv->parse->width * serv->parse->height) / 2;

	for (int i = 0; map[i]; i++)
		for (int j = 0; map[i][j]; j++)
			add_tile(&stock, map[i][j]);
	(stock.food < max ? add_map(serv, serv->map, 0) : 0);
	(stock.linemate < max ? add_map(serv, serv->map, 1) : 0);
	(stock.deraumere < max ? add_map(serv, serv->map, 2) : 0);
	(stock.sibur < max ? add_map(serv, serv->map, 3) : 0);
	(stock.mendiane < max ? add_map(serv, serv->map, 4) : 0);
	(stock.phiras < max ? add_map(serv, serv->map, 5) : 0);
	(stock.thystam < max ? add_map(serv, serv->map, 6) : 0);
}