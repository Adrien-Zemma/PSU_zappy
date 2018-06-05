/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Main C file
*/

#include "map.h"

void	gen_tile(tile_t **node)
{
	(*node)->linemate = ADD_MINERAL(0, 2);
	(*node)->deraumere = ADD_MINERAL(0, 2);
	(*node)->sibur = ADD_MINERAL(0, 2);
	(*node)->mendiane = ADD_MINERAL(0, 2);
	(*node)->phiras = ADD_MINERAL(0, 2);
	(*node)->thystam = ADD_MINERAL(0, 2);
}

tile_t	**gen_line(int w)
{
	tile_t	**node = malloc(sizeof(tile_t *) * (w + 1));

	if (!node)
		return NULL;
	for (int i = 0; i < w; i++) {
		node[i] = malloc(sizeof(tile_t));
		if (!node[i])
			return NULL;
		gen_tile(&node[i]);
	}
	node[w] = NULL;
	return node;
}

tile_t	***init_map(int weight, int height)
{
	tile_t	***tiles = malloc(sizeof(tile_t **) * (height + 1));

	if (!tiles)
		return NULL;
	for (int i = 0; i < height; i++) {
		tiles[i] = gen_line(weight);
		if (!tiles[i])
			return NULL;
	}
	tiles[height] = NULL;
	return tiles;
}

void	free_map(tile_t ***map)
{
	for (int i = 0; map[i]; i++) {
		for (int j = 0; map[i][j]; j++)
			free(map[i][j]);
		free(map[i]);
	}
	free(map);
}

int main(int ac, char **av)
{
	if (ac != 3)
		return 1;
	srand(time(NULL));
	tile_t ***map = init_map(atoi(av[1]), atoi(av[2]));
	if (!map)
		return 1;
	for (int i = 0; map[i]; i++) {
		for (int j = 0; map[i][j]; j++)
			printf("%d=>", map[i][j]->linemate);
	}
	free_map(map);
}