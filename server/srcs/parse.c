/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Parse C file
*/

#include "parse.h"

static void	add_arg(t_parse *obj, int id, char **av)
{
	if (!av[1])
		return;
	switch (id) {
		case 0:
		obj->port = atoi(av[1]);
		break;
		case 1:
		obj->width = atoi(av[1]);
		break;
		case 2:
		obj->height = atoi(av[1]);
		break;
		case 4:
		obj->max_client = atoi(av[1]);
		break;
		case 5:
		obj->freq = atoi(av[1]);
	}
}

static t_parse	*init_parse_struct(void)
{
	t_parse	*obj = malloc(sizeof(t_parse));

	obj->port = -1;
	obj->width = -1;
	obj->height = -1;
	obj->teams = NULL;
	obj->max_client = -1;
	obj->freq = -1;
	return (obj);
}

static char	**get_names_team(char **av)
{
	char	**names = calloc(1, sizeof(char *));
	char **tmp = av;
	int	i = 0;

	for (; *tmp; tmp++)
		if (strcmp("-n", *tmp) == 0)
			break;
	if (!*tmp)
		return (names);
	for (++tmp; *tmp; tmp++) {
		if (*tmp[0] == '-')
			break;
		else {
			names[i] = strdup(*tmp);
			i++;
			names = realloc(names, sizeof(char *) * (i + 1));
		}
	}
	names[i] = NULL;
	return (names);
}

static t_parse *check_parse_struct(t_parse *obj)
{
	if (obj->port == -1 || obj->width == -1 ||
	obj->height == -1 || !obj->teams ||
	obj->max_client == -1 || obj->freq == -1) {
		if (obj->teams)
			free_tab(obj->teams);
		free(obj);
		obj = NULL;
	}
	else {
		printf("Port: %d\nWidth: %d\nHeight: %d\nclientsNb: %d\nFreq: %d\n",
			obj->port, obj->width, obj->height, obj->max_client, obj->freq);
		printf("Names: ");
		for (int i = 0; obj->teams[i]; i++)
			printf("%s => ", obj->teams[i]);
	}
	return (obj);
}

t_parse	*parse_args(char **av)
{
	t_parse	*obj = init_parse_struct();
	int	id;

	if (!obj)
		return (NULL);
	obj->teams = get_names_team(av);
	if (!obj->teams)
		free(obj->teams);
	for (char **tmp = av; *tmp; tmp++) {
		id = check_arg(*tmp);
		if (id >= 0)
			add_arg(obj, id, tmp);
	}
	return (check_parse_struct(obj));
}
