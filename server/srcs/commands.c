/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Commands C file
*/

#include "commands.h"

command_t	**init_commands(void)
{
	const int	i = 14;
	command_t	**node = malloc(sizeof(command_t *) * (i + 1));

	if (!node)
		return NULL;
	node[0] = append_command("msz", map_size);
	node[1] = append_command("tna", names_team);
	node[2] = append_command("mct", map_content);
	node[3] = append_command("bct", tile_content);
	node[4] = append_command("plv #", player_level);
	node[5] = append_command("pin #", player_inventory);
	node[6] = append_command("ppo #", player_position);
	node[7] = append_command("Forward", forward);
	node[8] = append_command("Right", right);
	node[9] = append_command("Left", left);
	node[10] = append_command("inventory", inventory);
	node[11] = append_command("Look", look);
	node[12] = append_command("Broadcast", broadcast);
	node[13] = append_command("Take", take_object);
	node[i] = NULL;
	return node;
}

command_t	*append_command(char *name, int (*ptrFnct)(server_t *, client_t *, char *))
{
	command_t	*node = malloc(sizeof(command_t));

	if (!node)
		return NULL;
	node->name = name;
	node->ptrFnct = ptrFnct;
	return node;
}
