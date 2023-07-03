from Models.glcModel import glcModel
from Models.apModel import apModel


class Procesador:

    @staticmethod
    def data_processor(data, case, glc_array, ap_array):

        # Flags glc
        f_automataGL = False
        f_noTerminal = False
        f_terminal = False
        f_inicial = False
        f_producciones = False

        final_automata = False

        # Values glc
        nombre_valorAutomataGL = ""
        inicial_valor = ""

        # Transiciones glc
        noTerminal_valor = ""
        noTerminal_list = []

        terminal_valor = ""
        terminal_list = []

        producciones_valor = ""
        producciones_list = []

        # Flags ap
        f_automataP = False
        f_alfabeto = False
        f_simbolo = False
        f_estado = False
        f_eInicial = False
        f_eAceptacion = False
        f_transicion = False

        f_end_automaton = False

        # Values ap
        nombre_valorAutomataP = ""
        alfabeto_valor = ""
        simbolo_valor = ""
        estados_valor = ""
        eInicial_valor = ""

        # Estados de aceptación ap
        eAceptacion_valor = ""
        eAceptacion_list = []

        # Transiciones ap
        transicion_valor = ""
        transicion_list = []

        # Init of processor
        if case == 1:
            for letter in data:
                if f_automataGL == False:
                    if letter != '\n':
                        nombre_valorAutomataGL += letter
                    else:
                        f_automataGL = True

                elif f_noTerminal == False:
                    if letter != '\n':
                        if letter != ",":
                            noTerminal_valor += letter
                        else:
                            noTerminal_list.append(noTerminal_valor)
                            noTerminal_valor = ""

                    else:
                        noTerminal_list.append(noTerminal_valor)
                        noTerminal_valor = ""
                        f_noTerminal = True

                elif f_terminal == False:
                    if letter != '\n':
                        if letter != ",":
                            terminal_valor += letter
                        else:
                            terminal_list.append(terminal_valor)
                            terminal_valor = ""

                    else:
                        terminal_list.append(terminal_valor)
                        terminal_valor = ""
                        f_terminal = True

                elif f_inicial == False:
                    if letter != '\n':
                        inicial_valor += letter
                    else:
                        f_inicial = True

                elif f_producciones == False:
                    if letter != '%':
                        if letter != '\n':
                            producciones_valor += letter
                        else:
                            producciones_list.append(producciones_valor)
                            producciones_valor = ""

                    else:
                        new_glc = glcModel(nombre_valorAutomataGL, noTerminal_list, terminal_list, inicial_valor, producciones_list)
                        glc_array.append(new_glc)
                        f_producciones = True

                elif final_automata == False:
                    # Initialization var
                    f_automataGL = False
                    f_noTerminal = False
                    f_terminal = False
                    f_inicial = False
                    f_producciones = False

                    # Values
                    nombre_valorAutomataGL = ""
                    noTerminal_valor = ""
                    inicial_valor = ""

                    noTerminal_list = []
                    terminal_list = []
                    producciones_list = []

        elif case == 2:
            for letter in data:
                if f_automataP == False:
                    if letter != '\n':
                        nombre_valorAutomataP += letter
                    else:
                        f_automataP = True

                elif f_alfabeto == False:
                    if letter != '\n':
                        alfabeto_valor += letter
                    else:
                        f_alfabeto = True

                elif f_simbolo == False:
                    if letter != '\n':
                        simbolo_valor += letter
                    else:
                        f_simbolo = True

                elif f_estado == False:
                    if letter != '\n':
                        estados_valor += letter
                    else:
                        f_estado = True

                elif f_eInicial == False:
                    if letter != '\n':
                        eInicial_valor += letter
                    else:
                        f_eInicial = True

                elif f_eAceptacion == False:
                    if letter != '\n':
                        if letter != ",":
                            eAceptacion_valor += letter
                        else:
                            eAceptacion_list.append(eAceptacion_valor)
                            eAceptacion_valor = ""

                    else:
                        eAceptacion_list.append(eAceptacion_valor)
                        eAceptacion_valor = ""
                        f_eAceptacion = True

                elif f_transicion == False:
                    if letter != '%':
                        if letter != '\n':
                            transicion_valor += letter
                        else:
                            transicion_list.append(transicion_valor)
                            transicion_valor = ""

                    else:
                        new_ap = apModel(nombre_valorAutomataP, alfabeto_valor, simbolo_valor, estados_valor,  eInicial_valor, eAceptacion_list, transicion_list)
                        ap_array.append(new_ap)
                        f_transicion = True

                elif f_end_automaton == False:
                    # Initialization var
                    f_automataP = False
                    f_alfabeto = False
                    f_simbolo = False
                    f_estado = False
                    f_eInicial = False
                    f_eAceptacion = False
                    f_transicion = False

                    # Values
                    nombre_valorAutomataP = ""
                    alfabeto_valor = ""
                    simbolo_valor = ""
                    estados_valor = ""
                    eInicial_valor = ""

                    eAceptacion_list = []
                    transicion_list = []

        return (glc_array, ap_array)