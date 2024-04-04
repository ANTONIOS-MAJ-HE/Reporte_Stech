class Program
{
    static async Task Main(string[] args)
    {
        Console.WriteLine("Seleccione una opción:");
        Console.WriteLine("1. Insertar órdenes");
        Console.WriteLine("2. Insertar ventas diarias");
        Console.WriteLine("3. Insertar órdenes y ventas diarias");
        Console.Write("Ingrese el número de opción deseado: ");

        string opcion = Console.ReadLine();

        switch (opcion)
        {
            case "1":
                await InsertarOrdenes();
                break;
            case "2":
                await InsertarVentasDiarias();
                break;
            case "3":
                await InsertarOrdenesYVentasDiarias();
                break;
            default:
                Console.WriteLine("Opción no válida. Por favor, seleccione una opción válida.");
                break;
        }
    }

    static async Task InsertarOrdenes()
    {
        Console.WriteLine("Obteniendo datos de la orden de la base de datos...");

        // Consultar la base de datos para obtener los datos de la orden
        List<Orden> ordenes = await D_Orden.ObtenerOrdenesDesdeBaseDeDatos();

        // Insertar cada orden en la base de datos
        foreach (var orden in ordenes)
        {
            await N_Orden.InsertarOrden(orden);
        }

        Console.WriteLine("Órdenes insertadas correctamente.");
    }

    static async Task InsertarVentasDiarias()
    {
        Console.WriteLine("Obteniendo datos de ventas diarias de la base de datos...");

        // Consultar la base de datos para obtener los datos de ventas diarias
        List<VentaDia> ventaDias = await D_Orden.ObtenerVentasDiariasDesdeBaseDeDatos();

        // Insertar cada venta diaria en la base de datos
        foreach (var ventaDia in ventaDias)
        {
            await N_Orden.InsertarVentaDia(ventaDia);
        }

        Console.WriteLine("Ventas diarias insertadas correctamente.");
    }

    static async Task InsertarOrdenesYVentasDiarias()
    {
        await InsertarOrdenes();
        await InsertarVentasDiarias();
    }
}
