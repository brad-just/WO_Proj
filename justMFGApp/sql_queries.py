def build_sql_query_gen(department, field=None, sort_dir=None, ItemID=None):
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
	    dbo.timItemDescription.LongDesc,
        dbo.tmfWorkOrdHead_HAI.WorkOrderKey
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


    if(ItemID):
        ItemID_component = """AND dbo.timItem.ItemID LIKE '{}'""".format(ItemID)
    else:
        ItemID_component = ""

    if(department=="Custom"):
        query = base_component + " " + custom_component + " " + ItemID_component + " " + sort_component + ";"
    elif(department=="Bowl"):
        query = base_component + " " + bowl_component + " " + ItemID_component + " " + sort_component + ";"
    else:
        query = base_component + " " + general_component + " " + ItemID_component + " " + sort_component + ";"

    return(query)

def build_sql_query_bowlcust(field=None, sort_dir=None, ItemID=None):
    base_component = """
                    SELECT
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
                	    dbo.timItemDescription.LongDesc,
                        dbo.tmfWorkOrdHead_HAI.WorkOrderKey
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
                    WHERE dbo.tmfWorkOrdHead_HAI.Complete=0
                    AND dbo.tmfMfItemClass_HAI.MnfItemClassID LIKE 'BOWLCUST'
                    """

    if(field):
        if(sort_dir):
            direction = "DESC"
        else:
            direction = "ASC"
        sort_component = "ORDER BY {} {}".format(field, direction)
    else:
        sort_component = ""

    if(ItemID):
        ItemID_component = """AND dbo.timItem.ItemID LIKE '{}'""".format(ItemID)
    else:
        ItemID_component = ""

    query = base_component + " " + ItemID_component + " " + sort_component + ";"

    return(query)

def replenishments_query():
    query = '''SELECT * FROM
            	(SELECT

            		ItemID,
            		ShortDesc,
            		CAST(ISNULL(QtyOnHand, 0) AS DECIMAL(16,1)) AS QtyOnHand,
            		CAST(QtyOnPO AS DECIMAL(16,1)) AS QtyOnPO,
            		CAST(QtyOnWO AS DECIMAL(16,1)) AS QtyOnWO,
            		CAST(QtyOnSO AS DECIMAL(16,1)) AS QtyOnSO,
            		CAST(QtyReqForWO AS DECIMAL(16,1)) AS QtyReqForWO,
            		CAST((ISNULL(QtyOnHand, 0) + ISNULL(PendQtyIncrease, 0) - ISNULL(PendQtyDecrease, 0) + QtyOnPO + QtyOnWO - QtyOnSO - QtyReqForWO
            			- MinStockQty) AS DECIMAL(16,1)) AS ReOrderPosition

            	FROM

            	(SELECT
            		dbo.timItem.ItemID,
            		dbo.timItemDescription.ShortDesc,
            		dbo.timInventory.WhseKey,
            		dbo.timInventory.ItemKey,
            		dbo.timInventory.QtyOnPO,
            		dbo.timInventory.QtyOnWO,
            		dbo.timInventory.QtyOnSO,
            		dbo.timInventory.QtyReqForWO,
            		dbo.timInventory.MinStockQty
            	FROM dbo.timInventory
            	LEFT JOIN dbo.timItem
            	ON dbo.timInventory.ItemKey=dbo.timItem.ItemKey
            	LEFT JOIN dbo.timItemDescription
            	ON dbo.timInventory.ItemKey=dbo.timItemDescription.ItemKey
            	WHERE dbo.timInventory.WhseKey=24) a

            	FULL JOIN

            		(SELECT
            			dbo.timWhseBinInvt.ItemKey,
            			SUM(dbo.timWhseBinInvt.QtyOnHand) AS QtyOnHand,
            			SUM(dbo.timWhseBinInvt.PendQtyIncrease) AS PendQtyIncrease,
            			SUM(dbo.timWhseBinInvt.PendQtyDecrease) AS PendQtyDecrease
            		FROM dbo.timWhseBinInvt
            		LEFT JOIN dbo.timWhseBin
            		ON dbo.timWhseBinInvt.WhseBinKey=dbo.timWhseBin.WhseBinKey
            		WHERE timWhseBin.WhseKey=24
            		GROUP BY dbo.timWhseBinInvt.ItemKey) b
            	ON a.ItemKey=b.ItemKey) c
            WHERE ReOrderPosition<0;'''
    return(query)

def material_items_query(WorkOrderKey):
    query = '''
            SELECT
                dbo.tmfWorkOrdDetl_HAI.StepID,
            	dbo.timItemDescription.ShortDesc,
            	dbo.timItemDescription.LongDesc,
            	dbo.tmfWorkOrdDetl_HAI.OperationDesc1
            FROM dbo.tmfWorkOrdDetl_HAI
            LEFT JOIN dbo.timItemDescription
            ON dbo.tmfWorkOrdDetl_HAI.MatItemKey=dbo.timItemDescription.ItemKey
            WHERE dbo.tmfWorkOrdDetl_HAI.WorkOrderKey={}
            AND dbo.tmfWorkOrdDetl_HAI.StepComplete=0
            ORDER BY dbo.tmfWorkOrdDetl_HAI.StepID;
            '''.format(WorkOrderKey)
    return(query)

def get_orders_by_operation(operation):
    query='''
            SELECT
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
                dbo.timItemDescription.LongDesc,
                dbo.tmfWorkOrdHead_HAI.WorkOrderKey
            FROM dbo.tmfWorkOrdHead_HAI
            	LEFT JOIN dbo.tmfMfItemClass_HAI
            		ON dbo.tmfWorkOrdHead_HAI.ItemClassKey=dbo.tmfMfItemClass_HAI.ItemClassKey
            	LEFT JOIN dbo.tmfWorkOrdProd_HAI
            		ON dbo.tmfWorkOrdHead_HAI.WorkOrderKey=dbo.tmfWorkOrdProd_HAI.WorkOrderKey
            	LEFT JOIN dbo.tmfWorkOrdDetl_HAI
            		ON dbo.tmfWorkOrdHead_HAI.WorkOrderKey=dbo.tmfWorkOrdDetl_HAI.WorkOrderKey
            	LEFT JOIN dbo.tmfOperation_HAI
            		ON dbo.tmfWorkOrdDetl_HAI.OperationKey=dbo.tmfOperation_HAI.OperationKey
            	LEFT JOIN dbo.timItemDescription
            		ON dbo.tmfWorkOrdProd_HAI.ItemKey=dbo.timItemDescription.ItemKey
            	LEFT JOIN dbo.timItem
            		ON dbo.timItemDescription.ItemKey=dbo.timItem.ItemKey
            	LEFT JOIN dbo.tsoSalesOrder
            		ON dbo.tmfWorkOrdProd_HAI.SOKey=dbo.tsoSalesOrder.SOKey
            	LEFT JOIN dbo.tsoSOLine
            		ON 	dbo.tmfWorkOrdProd_HAI.SOLineKey=dbo.tsoSOLine.SOLineKey
            WHERE dbo.tmfWorkOrdHead_HAI.Complete=0
            AND dbo.tmfWorkOrdDetl_HAI.StepComplete=0
            AND (dbo.tmfMfItemClass_HAI.MnfItemClassID LIKE '%CUST%' OR dbo.tmfMfItemClass_HAI.MnfItemClassID LIKE '%BOWL%')
            AND dbo.tmfOperation_HAI.OperationID='{}';
          '''.format(operation)

    return(query)
