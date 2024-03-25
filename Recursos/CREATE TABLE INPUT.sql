USE [DB_ST]
GO

/****** Object:  Table [dbo].[ST_CONS_ORDENES_NEW]    Script Date: 14/03/2024 11:32:10 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[ST_CONS_ORDENES_NEW](
	[CANAL] [varchar](8000) NOT NULL,
	[NUMERO_ORDEN] [varchar](8000) NULL,
	[NUMERO_FACTURA] [varchar](8000) NULL,
	[DNI_CLIENTE] [varchar](8000) NULL,
	[NOMBRE_CLIENTE] [varchar](8000) NULL,
	[DIRECCION_CLIENTE] [varchar](8000) NULL,
	[REGION_VENTA] [varchar](8000) NULL,
	[NOMBRE_PRODUCTO] [varchar](8000) NULL,
	[MODELO_PRODUCTO] [varchar](8000) NULL,
	[MARCA_PRODUCTO] [varchar](8000) NULL,
	[CATEGORIA_PRODUCTO] [varchar](8000) NULL,
	[CODIGO_PRODUCTO_CANAL] [varchar](8000) NULL,
	[PART_NUMBER] [varchar](8000) NULL,
	[CANTIDAD] [varchar](8000) NULL,
	[PRECIO_S_IGV] [varchar](8000) NULL,
	[PRECIO_C_IGV] [varchar](8000) NULL,
	[TOTAL_S_IGV] [varchar](8000) NULL,
	[TOTAL_C_IGV] [varchar](8000) NULL,
	[FECHA_ORDEN] [varchar](8000) NULL,
	[FECHA_PROCESO] [varchar](8000) NULL,
	[FECHA_DESPACHO] [varchar](8000) NULL,
	[ST_DESPACHO] [varchar](8000) NULL,
	[ESTADO_ORDEN] [varchar](8000) NULL,
	[OBSERVACION_ORDEN] [varchar](8000) NULL,
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


