def build_sql_query_gen(department, field=None, sort_dir=None):
    base_component = """SELECT
    	REPLACE(LTRIM(REPLACE(dbo.tsoSalesOrder.TranNoRel,'0',' ')),' ','0') AS TranNoRel,
	    dbo.tsoSOLine.SOLineNo,
	    dbo.timItem.ItemID,
	    dbo.timItemDescription.ShortDesc,
	    CAST(dbo.tmfWorkOrdHead_HAI.Quantity AS DECIMAL(16,1)) AS Quantity,
    	CAST(dbo.tmfWorkOrdHead_HAI.QuantityToDate AS DECIMAL(16,1)) AS QuantityToDate,
    	REPLACE(LTRIM(REPLACE(dbo.tmfWorkOrdHead_HAI.WorkOrderNo,'0',' ')),' ','0') AS WorkOrderNo,
    	dbo.tmfWorkOrdHead_HAI.CustPONo,
    	CAST(dbo.tmfWorkOrdHead_HAI.EntryDate AS DATE) AS EntryDate,
    	CAST(dbo.tmfWorkOrdHead_HAI.ActualStartDate AS DATE) AS ActualStartDate,
    	CAST(dbo.tmfWorkOrdHead_HAI.MFGCommitDate AS DATE) AS MFGCommitDate,
    	CAST(dbo.tmfWorkOrdHead_HAI.ReleaseDate AS DATE) AS ReleaseDate,
    	CAST(dbo.tmfWorkOrdHead_HAI.RequiredDate AS DATE) AS RequiredDate,
    	dbo.tsoSalesOrder.Hold,
    	dbo.tsoSalesOrder.HoldReason,
	    dbo.tmfMfItemClass_HAI.MnfItemClassID,
	    dbo.timItemDescription.LongDesc
    FROM dbo.tmfWorkOrdHead_HAI
    	FULL JOIN dbo.tmfMfItemClass_HAI
    		ON dbo.tmfWorkOrdHead_HAI.ItemClassKey=dbo.tmfMfItemClass_HAI.ItemClassKey
    	FULL JOIN dbo.tmfWorkOrdProd_HAI
    		ON dbo.tmfWorkOrdHead_HAI.WorkOrderKey=dbo.tmfWorkOrdProd_HAI.WorkOrderKey
    	FULL JOIN dbo.timItemDescription
    		ON dbo.tmfWorkOrdProd_HAI.ItemKey=dbo.timItemDescription.ItemKey
    	FULL JOIN dbo.timItem
    		ON dbo.timItemDescription.ItemKey=dbo.timItem.ItemKey
    	FULL JOIN dbo.tsoSalesOrder
    		ON dbo.tmfWorkOrdProd_HAI.SOKey=dbo.tsoSalesOrder.SOKey
    	FULL JOIN dbo.tsoSOLine
    		ON 	dbo.tmfWorkOrdProd_HAI.SOLineKey=dbo.tsoSOLine.SOLineKey
    WHERE dbo.tmfWorkOrdHead_HAI.Complete=0"""

    custom_component = """AND dbo.tmfMfItemClass_HAI.MnfItemClassID LIKE 'CUSTOM'
                       AND dbo.tmfWorkOrdHead_HAI.CustPONo IS NOT NULL
                       AND dbo.tmfWorkOrdHead_HAI.CustPONo!=''"""

    bowl_component = """AND dbo.tmfMfItemClass_HAI.MnfItemClassID LIKE 'BOWL'"""

    general_component = """AND (dbo.tmfMfItemClass_HAI.MnfItemClassID LIKE 'CUSTOM' OR dbo.tmfMfItemClass_HAI.MnfItemClassID LIKE 'BOWL')"""

    if(field):
        if(sort_dir):
            direction = "DESC"
        else:
            direction = "ASC"
        sort_component = "ORDER BY {} {}".format(field, direction)
    else:
        sort_component = ""


    if(department=="Custom"):
        query = base_component + " " + custom_component + " " + sort_component + ";"
    elif(department=="Bowl"):
        query = base_component + " " + bowl_component + " " + sort_component + ";"
    else:
        query = base_component + " " + general_component + " " + sort_component + ";"

    return(query)

def build_sql_query_bowlcust(department, field=None, sort_dir=None):
    base_component = """SELECT
    	REPLACE(LTRIM(REPLACE(dbo.tsoSalesOrder.TranNoRel,'0',' ')),' ','0') AS TranNoRel,
	    dbo.tsoSOLine.SOLineNo,
	    dbo.timItem.ItemID,
	    dbo.timItemDescription.ShortDesc,
	    CAST(dbo.tmfWorkOrdHead_HAI.Quantity AS DECIMAL(16,1)) AS Quantity,
    	CAST(dbo.tmfWorkOrdHead_HAI.QuantityToDate AS DECIMAL(16,1)) AS QuantityToDate,
    	REPLACE(LTRIM(REPLACE(dbo.tmfWorkOrdHead_HAI.WorkOrderNo,'0',' ')),' ','0') AS WorkOrderNo,
    	dbo.tmfWorkOrdHead_HAI.CustPONo,
    	CAST(dbo.tmfWorkOrdHead_HAI.EntryDate AS DATE) AS EntryDate,
    	CAST(dbo.tmfWorkOrdHead_HAI.ActualStartDate AS DATE) AS ActualStartDate,
    	CAST(dbo.tmfWorkOrdHead_HAI.MFGCommitDate AS DATE) AS MFGCommitDate,
    	CAST(dbo.tmfWorkOrdHead_HAI.ReleaseDate AS DATE) AS ReleaseDate,
    	CAST(dbo.tmfWorkOrdHead_HAI.RequiredDate AS DATE) AS RequiredDate,
    	dbo.tsoSalesOrder.Hold,
    	dbo.tsoSalesOrder.HoldReason,
	    dbo.tmfMfItemClass_HAI.MnfItemClassID,
	    dbo.timItemDescription.LongDesc
    FROM dbo.tmfWorkOrdHead_HAI
    	FULL JOIN dbo.tmfMfItemClass_HAI
    		ON dbo.tmfWorkOrdHead_HAI.ItemClassKey=dbo.tmfMfItemClass_HAI.ItemClassKey
    	FULL JOIN dbo.tmfWorkOrdProd_HAI
    		ON dbo.tmfWorkOrdHead_HAI.WorkOrderKey=dbo.tmfWorkOrdProd_HAI.WorkOrderKey
    	FULL JOIN dbo.timItemDescription
    		ON dbo.tmfWorkOrdProd_HAI.ItemKey=dbo.timItemDescription.ItemKey
    	FULL JOIN dbo.timItem
    		ON dbo.timItemDescription.ItemKey=dbo.timItem.ItemKey
    	FULL JOIN dbo.tsoSalesOrder
    		ON dbo.tmfWorkOrdProd_HAI.SOKey=dbo.tsoSalesOrder.SOKey
    	FULL JOIN dbo.tsoSOLine
    		ON 	dbo.tmfWorkOrdProd_HAI.SOLineKey=dbo.tsoSOLine.SOLineKey
    WHERE dbo.tmfWorkOrdHead_HAI.Complete=0"""

    custom_component = """AND dbo.tmfMfItemClass_HAI.MnfItemClassID LIKE 'BOWLCUST'
                       AND dbo.tmfWorkOrdHead_HAI.CustPONo IS NOT NULL
                       AND dbo.tmfWorkOrdHead_HAI.CustPONo!=''"""

    bowl_component = """AND dbo.tmfMfItemClass_HAI.MnfItemClassID LIKE 'BOWLCUST'"""

    general_component = """AND dbo.tmfMfItemClass_HAI.MnfItemClassID LIKE 'BOWLCUST'"""

    if(field):
        if(sort_dir):
            direction = "DESC"
        else:
            direction = "ASC"
        sort_component = "ORDER BY {} {}".format(field, direction)
    else:
        sort_component = ""


    if(department=="Custom"):
        query = base_component + " " + custom_component + " " + sort_component + ";"
    elif(department=="Bowl"):
        query = base_component + " " + bowl_component + " " + sort_component + ";"
    else:
        query = base_component + " " + general_component + " " + sort_component + ";"

    return(query)
