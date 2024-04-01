using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        Console.WriteLine("Ingrese los datos de la orden:");

        // Solicitar entrada de datos al usuario
        Console.Write("Canal: ");
        string canal = Console.ReadLine();

        Console.Write("Numero Orden: ");
        string numero_orden = Console.ReadLine();
        // Solicitar el resto de los datos de la orden...

        // Crear un objeto Orden con los datos ingresados
        Orden orden = new Orden
        {
            canal = canal,
            numero_orden = numero_orden,
            // Asignar el resto de los datos de la orden...
        };

        // Insertar la orden en la base de datos
        await InsertarOrden(orden);

        Console.WriteLine("Orden insertada correctamente.");
    }

    static async Task InsertarOrden(Orden orden)
    {
        using (HttpClient client = new HttpClient())
        {
            client.BaseAddress = new Uri("http://localhost:8000/");
            client.DefaultRequestHeaders.Accept.Clear();
            client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

            try
            {
                string authToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyOTE0MTg2LCJpYXQiOjE3MTEzNzgxODYsImp0aSI6IjNjODMxMDM1MWFiZTRiZDA5OTIzODE4ODg4NzFjMWNjIiwidXNlcl9pZCI6MX0.3c7Hn9YZvW7GXy0CmgZyMKZWwpyypuZs773cKoLFg8s";

                // Agregar el token de autenticación al encabezado
                client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", authToken);

                HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Post, "ordenes/");
                request.Content = new StringContent(JsonConvert.SerializeObject(orden), Encoding.UTF8, "application/json");

                HttpResponseMessage response = await client.SendAsync(request);

                response.EnsureSuccessStatusCode();
            }
            catch (HttpRequestException e)
            {
                Console.WriteLine($"Error al insertar la orden: {e.Message}");
            }
        }
    }
}

public class Orden
{
    public string canal { get; set; }
    public string numero_orden { get; set; }
    // Agregar el resto de las propiedades de la orden...
}