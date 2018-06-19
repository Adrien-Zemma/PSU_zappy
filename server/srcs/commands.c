/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Commands C file
*/

#include "commands.h"
#include "parse.h"

command_t	**init_commands(t_parse *parse)
{
	const int	i = 14;
	command_t	**node = malloc(sizeof(command_t *) * (i + 1));

	if (!node)
		return NULL;
	node[0] = append_command("msz", map_size, 0);
	node[1] = append_command("tna", names_team, 0);
	node[2] = append_command("mct", map_content, 0);
	node[3] = append_command("bct", tile_content, 0);
	node[4] = append_command("plv #", player_level, 0);
	node[5] = append_command("pin #", player_inventory, 0);
	node[6] = append_command("ppo #", player_position, 0);
	node[7] = append_command("Forward", forward, 7 / (double)parse->freq);
	node[8] = append_command("Right", right , 7 / (double)parse->freq);
	node[9] = append_command("Left", left, 7 / (double)parse->freq);
	node[10] = append_command("inventory", inventory, 1 / (double)parse->freq);
	node[11] = append_command("Look", look, 7 / (double)parse->freq);
	node[12] = append_command("Broadcast", broadcast, 7 / (double)parse->freq);
	node[13] = append_command("Take", take_object, 7 / (double)parse->freq);
	node[i] = NULL;
	return node;
}

command_t	*append_command(char *name, int (*ptrFnct)(server_t *, client_t *, char *), double time)
{
	command_t	*node = malloc(sizeof(command_t));

	if (!node)
		return NULL;
	node->time = time;
	node->name = name;
	node->ptrFnct = ptrFnct;
	return node;
}
