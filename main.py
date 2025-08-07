def seleccionar_puerto_spring():
    while True:
        try:
            puerto_spring = int(
                input("⚙️ Digite el número del puerto de Spring Boot (1-65535): ")
            )
            if 1 <= puerto_spring <= 65535:
                break
            else:
                print("❌ El puerto debe estar entre 1 y 65535")
        except ValueError:
            print("❌ Tiene que digitar un valor numérico")

    return {"server.port": str(puerto_spring)}


def seleccion_base_datos():
    while True:
        base_datos = input(
            "🗄️ ¿Qué base de datos desea usar? 'mysql' o 'postgres': "
        ).strip()
        if not base_datos:
            print("⚠️ Debe ingresar un valor.")
            continue
        match base_datos[0].upper():
            case "M":
                return base_datos_mysql()
            case "P":
                return base_datos_postgres()
            case _:
                print("❌ Opción inválida. Digite 'mysql' o 'postgres'.")


def base_datos_mysql():
    response = input(
        "✍️ ¿Quiere introducir los datos? (Enter para usar valores por defecto): "
    )
    if response:
        while True:
            username = input(
                "👤 Digite el username de su base de datos MySQL: "
            ).strip()
            if username:
                break
            print("⚠️ El username no puede estar vacío.")

        password = input("🔑 Digite el password de su base de datos MySQL: ").strip()

        host = input(
            "🏠 Digite la dirección del host de la base de datos (por defecto 'localhost'): "
        ).strip()
        if not host:
            host = "localhost"

        port = input(
            "🔢 Digite el puerto de la base de datos (por defecto 3306): "
        ).strip()
        if not port:
            port = "3306"

        while True:
            database_name = input("📛 Digite el nombre de su base de datos: ").strip()
            if database_name:
                break
            print("⚠️ El nombre de la base de datos no puede estar vacío.")

        jdbc_url = f"jdbc:mysql://{host}:{port}/{database_name}"
    else:
        username = "root"
        password = "root"
        jdbc_url = "jdbc:mysql://localhost:3306/basedatos"

    return {
        "spring.datasource.url": jdbc_url,
        "spring.datasource.username": username,
        "spring.datasource.password": password,
        "spring.datasource.driver-class-name": "com.mysql.cj.jdbc.Driver",
    }


def base_datos_postgres():
    response = input(
        "✍️ ¿Quiere introducir los datos? (Enter para usar valores por defecto): "
    )
    if response:
        while True:
            username = input(
                "👤 Digite el username de su base de datos PostgreSQL: "
            ).strip()
            if username:
                break
            print("⚠️ El username no puede estar vacío.")

        password = input(
            "🔑 Digite el password de su base de datos PostgreSQL: "
        ).strip()

        host = input(
            "🏠 Digite la dirección del host de la base de datos PostgreSQL (por defecto 'localhost'): "
        ).strip()
        if not host:
            host = "localhost"

        port = input(
            "🔢 Digite el puerto de la base de datos PostgreSQL (por defecto 5432): "
        ).strip()
        if not port:
            port = "5432"

        while True:
            database_name = input(
                "📛 Digite el nombre de su base de datos PostgreSQL: "
            ).strip()
            if database_name:
                break
            print("⚠️ El nombre de la base de datos no puede estar vacío.")

        jdbc_url = f"jdbc:postgresql://{host}:{port}/{database_name}"
    else:
        username = "postgre"
        password = "postgre"
        jdbc_url = "jdbc:postgresql://localhost:5432/postgre"

    return {
        "spring.datasource.url": jdbc_url,
        "spring.datasource.username": username,
        "spring.datasource.password": password,
        "spring.datasource.driver-class-name": "org.postgresql.Driver",
    }


def main():
    print("🚀 Configuración de Spring Boot y Base de Datos\n")
    propiedades = seleccionar_puerto_spring()
    propiedades_db = seleccion_base_datos()
    propiedades.update(propiedades_db)

    print("\n✅ Contenido generado para application.properties:\n")
    for clave, valor in propiedades.items():
        print(f"{clave}={valor}")


if __name__ == "__main__":
    main()
