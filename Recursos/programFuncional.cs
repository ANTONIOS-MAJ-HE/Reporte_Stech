using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

using System;
using System.Net.Http;
using System.Threading.Tasks;
using System.Net.Http.Headers;

class Program
{
    static async Task Main(string[] args)
    {
        Console.WriteLine("Obteniendo datos de la orden de la base de datos...");

        // Consultar la base de datos para obtener los datos de la orden
        List<Orden> ordenes = await ObtenerOrdenesDesdeBaseDeDatos();

        // Insertar cada orden en la base de datos
        foreach (var orden in ordenes)
        {
            await InsertarOrden(orden);
        }

        Console.WriteLine("Órdenes insertadas correctamente.");
    }

    static async Task<List<Orden>> ObtenerOrdenesDesdeBaseDeDatos()
    {
        // Aquí implementas la lógica para consultar la base de datos y recuperar los datos de las órdenes
        // Por ejemplo:
        // 1. Conexión a la base de datos
        // 2. Ejecutar consulta SQL para obtener los datos de las órdenes
        // 3. Mapear los resultados de la consulta a objetos Orden y agregarlos a una lista

        List<Orden> ordenes = new List<Orden>();
        string connectionString = "Data Source=LAPTOP-R1VL050P\\SQLEXPRESS2017;Initial Catalog=DB_ST;Integrated Security=True;"; // Reemplazar con tu cadena de conexión

        using (SqlConnection connection = new SqlConnection(connectionString))
        {
            string query = "SELECT CANAL, NUMERO_ORDEN FROM ST_CONS_ORDENES_NEW WHERE NUMERO_ORDEN = '32760411' ORDER BY FECHA_PROCESO DESC;"; // Reemplazar con tu consulta SQL
            SqlCommand command = new SqlCommand(query, connection);

            try
            {
                connection.Open();
                SqlDataReader reader = command.ExecuteReader();
                while (reader.Read())
                {
                    Orden orden = new Orden
                    {
                        // Asignar los valores de las columnas de la tabla a las propiedades de la clase Orden
                        canal = reader["CANAL"].ToString(),
                        numero_orden = reader["NUMERO_ORDEN"].ToString(),
                    };
                    ordenes.Add(orden);
                }
                reader.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error al obtener las órdenes desde la base de datos: " + ex.Message);
            }
        }

        return ordenes;
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
    // Agregar el resto de las propiedades de la orden...
}