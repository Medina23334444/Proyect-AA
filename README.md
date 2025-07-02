# Probabilistic Deterministic Automaton

Este repositorio contiene una implementación sencilla en Python de un Autómata Probabilístico Determinista (APD) basado en la propuesta del usuario.

El archivo `automaton.py` define una clase `ProbabilisticDeterministicAutomaton` con los siguientes elementos:

- **Estados:** `S0` a `S11`.
- **Eventos (alfabeto):** `login`, `failed_login`, `read_file`, `write_file`, `upload_script`, `execute_binary`, `access_admin`, `create_user`, `change_config`, `open_port`, `download_data`, `logout`.
- **Estado inicial:** `S0`.
- **Estados de aceptación:** `S6`, `S7`, `S8`, `S9`, `S10`.
- **Transiciones con probabilidades:** codificadas según la tabla proporcionada.

## Uso rápido

```bash
python automaton.py
```

El script ejecutará un ejemplo de secuencia de eventos y mostrará el estado final, la probabilidad total de la secuencia y si dicho estado es de aceptación.

También se puede usar el módulo desde otro script importando la clase `ProbabilisticDeterministicAutomaton` y utilizando los métodos `process_event` o `process_sequence`.


## Integración con Flask

Se incluye un pequeño servidor Flask (`app.py`) que expone un endpoint `/process`. Este servicio permite enviar una secuencia de eventos en formato JSON y devuelve el estado final alcanzado, la probabilidad acumulada y si dicho estado es de aceptación.

### Ejecución

1. Instalar dependencias (solo Flask):

```bash
pip install Flask
```

2. Iniciar el servidor:

```bash
python app.py
```

3. Enviar una secuencia de ejemplo usando `curl` u otra herramienta:

```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"events": ["login", "read_file", "upload_script", "execute_binary"]}' \
     http://localhost:5000/process
```

El servicio responderá con un JSON que incluye el estado final, la probabilidad calculada y si se trata de un estado de aceptación.

