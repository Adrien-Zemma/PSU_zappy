/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Parse Header file
*/

#ifndef PARSE_H_
	#define PARSE_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct	s_parse
{
	int	port;
	int	width;
	int	height;
	char	**teams;
	int	clientsNb;
	int	freq;
}		t_parse;

t_parse	*parse_args(char **av);
int	check_arg(char *command);
void	free_tab(char **args);

extern const char commands_name[6][64];

#endif /* !PARSE_H_ */
