/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Main C file
*/

#include "commands.h"
#include "parse.h"

int main(int ac, char **av)
{
	t_parse	*parse = parse_args(av);

	if (!parse || ac < 12) {
		if (parse && parse->teams)
			free(parse->teams);
		free(parse);
		return (84);
	}
	init_commands();
	free_tab(parse->teams);
	free(parse);
	return (0);
}