/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Map H file
*/

#ifndef MAP_H_
	#define MAP_H_

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ADD_MINERAL(a, b)  (rand() % (b - a) + a)

typedef struct	tile {
	int	linemate;
	int	deraumere;
	int	sibur;
	int	mendiane;
	int	phiras;
	int	thystam;
}		tile_t;

#endif /* !MAP_H_ */
